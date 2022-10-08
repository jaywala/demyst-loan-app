import os
from flask import Flask, render_template, request, redirect, url_for, abort
from flask import Flask, session
from flask_session import Session
from .source.LoanApplication import LoanApplication
from .source.LoanSummary import LoanSummary

from logging.config import dictConfig


def create_app(test_config=None):
    dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
    })
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    @app.route('/set/')
    def set():
        session['key'] = 'value'
        return 'ok'

    @app.route('/get/')
    def get():
        return session.get('key', 'not set')


    @app.route('/',methods = ['GET', 'POST'])
    def home():
        # if request.method == 'POST':
        #     # if "confirm":
            # return render_template()
        return render_template('home.html')


    @app.route('/loan_application',methods = ['GET', 'POST'])
    def loan_application():
        if request.method == 'POST':
            app.logger.info(f"{request.form = }")
            if 'cancel' in request.form:
                return redirect(url_for('home'))
            elif 'request_balance_sheet' in request.form:
                session["buisness_name"] = request.form.get("buisness_name")
                session["loan_amount"] = request.form.get("loan_amount")
                session['asp'] = request.form.get("accounting_software")
                session['established_year'] = request.form.get("established_year")
                return redirect(url_for('balance_sheet'))
        return render_template('loan_application.html')


    @app.route('/balance_sheet', methods = ['GET', 'POST'])
    def balance_sheet():
        # balance_sheets_test = [{"month": "1/2020","profit": "100","asset_value": "-100"}, {"month": "2/2020","profit": "100","asset_value": "-100"}, {"month": "3/2020","profit": "100","asset_value": "-100"}]
        if "buisness_name" not in session:
            return redirect(url_for('home'))
        
        app.logger.info(f"{request.form = }")
        if request.method == 'POST':
            if 'submit' in request.form:
                return redirect(url_for('pre_assessment'))
        
        app.logger.info(f"{session['buisness_name']}, {session['loan_amount']}, {session['asp']}, {session['established_year']}")
        loan_application = LoanApplication(session['buisness_name'], session['loan_amount'], session['asp'], session['established_year'])
        return render_template('balance_sheet.html', buisness_name = session['buisness_name'], balance_sheets = loan_application.balance_sheet)


    @app.route('/pre_assessment', methods = ['GET'])
    def pre_assessment():
        if "buisness_name" not in session:
            return redirect(url_for('home')) 
        loan_application = LoanApplication(session['buisness_name'], session['loan_amount'], session['asp'], session['established_year'])
        pre_assessment = loan_application.calculatePreAssessment()
        loan_summary = LoanSummary(loan_application.buisness_name, loan_application.established_year, loan_application.calculateYearlyProfits(), loan_application.loan_amount, pre_assessment)
        # Mocking decision engine request was successful
        if loan_summary.sendSummaryToDecisionEngine() == True:
            return render_template('pre_assessment.html', pre_assessment = pre_assessment, loan_application = loan_application)
        else:
            return 'Submission failed! Please contact an admin'


    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return '404 page not found'


    return app