import flask
import services.dividend_profit_calculator as div_profit
from infrastructure.view_modifiers import response


blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home_page.html')
def index():
    div_data = div_profit.dividend_meta()
    return {'dividend_data': div_data} 
