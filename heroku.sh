heroku login
heroku container:login
heroku apps:destroy -a morse-douglas --confirm morse-douglas
heroku create morse-douglas
heroku container:push web -a morse-douglas
heroku container:release web -a morse-douglas
heroku open -a morse-douglas
