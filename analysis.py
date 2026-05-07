import pandas as pd

def analyze_results(total, user_answers, results):
    data = {
        "Question_No": list(range(1, total + 1)),
        "User_Answer": user_answers,
        "Result": results
    }

    df = pd.DataFrame(data)

    print("\n===== PERFORMANCE ANALYSIS =====")
    print(df)

    accuracy = (sum(results) / total) * 100
    print(f"\nAccuracy: {accuracy:.2f}%")
