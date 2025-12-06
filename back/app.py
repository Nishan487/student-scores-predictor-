from factory.processing import Processing 
from flask import Blueprint,jsonify,request

score_bp = Blueprint('score_bp', __name__)
@score_bp.route('/', methods=['GET','POST'])
def get_prediction():
    hours = request.args.get('hours', default=1, type=float)
    data = Processing.process('score.csv', hours)
    return jsonify({"data":data,'graph_url':'static/plot.png'}), 200

    
    