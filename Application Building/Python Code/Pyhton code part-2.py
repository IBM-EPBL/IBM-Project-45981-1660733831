if(y_pred == 0) :
    return render_template("0.html", showcase = str(y_pred))
  elif(y_pred == 1) :
    return render_template("1.html ", showcase = str(y_pred))
  elif(y_pred == 2) :
    return render_template("2.html", showcase = str(y_pred))
  elif(y_pred == 3) :
    return render_template("3.html", showcase = str(y_pred))
  elif(y_pred == 4) :
    return render_template("4.html", showcase = str(y_pred))
  elif(y_pred == 5) :
    return render_template("5.html", showcase = str(y_pred))
  elif(y_pred == 6) :
    return render_template("6.html", showcase = str(y_pred))
  elif(y_pred == 7) :
    return render_template("7.html", showcase = str(y_pred))
  elif(y_pred == 8) :
    return render_template("8.html", showcase = str(y_pred))
  else :
    return render_template("9.html", showcase = str(y_pred))
  


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000,debug=True,threaded=False)