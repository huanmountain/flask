from flask import Blueprint,render_template,request,flash
import DFA
from decorators import login_required


bp = Blueprint("laboratory", __name__, url_prefix="/laboratory")


@bp.route("/index", methods=['GET', 'POST'])
@login_required
# 装饰器,把public_question当作参数传入login_required
# @login_required
# 遇到public_question执行login_required(public_question)的返回值
def index():
    if request.method == 'GET':
        return render_template('laboratory.html')
    else:
          content = request.form.get('content')
          result1 = DFA.cut_deal(content)
          result2 =DFA.cuttest(content)
          # flash("分词结果为：" + content)
          flash("分词结果为："+ result1)
          flash("输出结果为：" + result2)
          return render_template('laboratory.html')









