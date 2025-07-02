def calculate_scores(answers):
    ga_score = int(answers.get('q1', 0)) + int(answers.get('q2', 0)) + int(answers.get('q3', 0))
    rs_score = int(answers.get('q4', 0)) + int(answers.get('q5', 0)) + int(answers.get('q6', 0)) + int(answers.get('q7', 0))
    return ga_score, rs_score
