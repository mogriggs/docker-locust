from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

def first(l):
    l.client.get("/first")

def second(l):
    l.client.get("/second")

class UserBehavior(TaskSet):
    tasks = {index: 3, first: 2, second: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
