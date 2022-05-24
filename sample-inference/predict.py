import pendulum


def predict(*args, **kwargs):
    print(args)
    print(kwargs)
    return {"score": 10}