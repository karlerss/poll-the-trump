from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from models import *

app = Flask(__name__)

init_db()


@app.route('/')
@cross_origin()
def hello_world():
    db_session().begin()
    sql = """select reply_id,
count(id) as count,
SUM(case when vote=1 then 1 else 0 end) as pos_votes,
SUM(case when vote=-1 then 1 else 0 end) as neg_votes ,
sum(abs(vote))/count(id)
from tweets where reply_id IS NOT NULL
group by reply_id
having count > 20 order by reply_id desc"""
    res = db_session().execute(sql)
    return jsonify(res)
