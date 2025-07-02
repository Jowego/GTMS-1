def calculate_scores(answers):
    ga_score = 0
    rs_score = 0
    for key, value in answers.items():
        if key.startswith('ga_'):
            ga_score += int(value)
        elif key.startswith('rs_'):
            rs_score += int(value)
    return ga_score, rs_score
