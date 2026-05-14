import json


def load_assessments():

    with open("app/data/assessments.json", "r") as file:
        return json.load(file)


def recommend_assessments(user_query):

    assessments = load_assessments()

    matched = []

    user_query = user_query.lower()

    for assessment in assessments:

        for skill in assessment["skills"]:

            if skill in user_query:

                matched.append({
                    "name": assessment["name"],
                    "url": assessment["url"],
                    "test_type": assessment["test_type"]
                })

                break

    return matched