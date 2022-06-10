function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function(event){
      var $this = $(this);
      var email = $("input[name ='email']").val();
      if(!email){
          alert("请输入邮箱");
          return;
      }
      // 通过js发送请求,ajax
        $.ajax({
            url:"/user/captcha",
            method:"POST",
            data:{
                "email":email
            },
            success: function (res){
                var code =res['code'];
                if(code == 200)
                {
                    //取消点击事件
                    $this.off("click");
                    var countDown = 60;
                    var timer = setInterval(function ()
                    {
                        countDown -= 1;
                        if(countDown > 0){
                            $this.text(countDown+"秒后重新发送");
                        }
                        else{
                            $this.text("获取验证码1");
                            //重新执行函数绑定点击事件
                            bindCaptchaBtnClick();
                            //清除倒计时
                            clearInterval(timer)
                        }
                    },1000);
                    alert("验证码发送成功")
                }
                else
                {
                    alert(res['message'])
                }

            }
        })

    });
}


$(function (){
    bindCaptchaBtnClick();
});

