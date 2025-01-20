from math_course.handlers.quiz import quiz_router
from math_course.handlers.user_flow import flow_router

routers = [
    flow_router,
    quiz_router,
]
