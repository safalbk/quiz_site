  // document.getElementById('post').onclick = () => {
  //   const requestObj = new XMLHttpRequest()
  //   requestObj.onreadystatechange = function () {
  //     if (this.readyState == 4 && this.status == 200) {
  //       console.log("hey this is response"+this.responseText)
  //       // const element = document.getElementById("html_delete");
  //       // element.remove();
  //       // document.write(this.responseText)
  //     }
  //   }

  //   requestObj.open("POST", "{% url 'quiz:vote' quiz.id current_question.question_num %}")
  //   requestObj.setRequestHeader("X-CSRFToken", csrftoken)

  //   const formdata = new FormData()
  //   formdata.append('choice', selected_choice)
  //   requestObj.send(formdata)
  // }
