# tinyfeet
Saw that an external form-filling procedure could be speeded up.
Tested how quickly this can be done.

Created a memcache at heroku using git bash -
heroku addons:create memcachier:dev --app resoler

heroku config
allows us to see the memcache pwd, servers and username
we can then amend our config file to gather these

records.txt
now redundant (and a few lines of code that go along with it)
see del_area

handy tip
when testing locally just hardwire the true memcache vars across from heroku

