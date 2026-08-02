from detoxify import Detoxify
import time

model = Detoxify("multilingual")

def detect(text):

    start_time = time.perf_counter()

    results = model.predict(text)

    end_time = time.perf_counter()

    final_time = f"\nAnalysis time : {end_time - start_time:.2f} s\n"

    sorted_results = sorted(

        results.items(),

        key=lambda item: item[1],

        reverse=True

    )

    categories = []

    for category, score in sorted_results:

        category = category.replace("_", " ").title()

        categories.append((category, score))

    max_length = max(len(category) for category, score in categories)

    result = ""

    for category, score in categories:

        dots = "." * (max_length - len(category) + 10)

        result += f"• {category}{dots}{score * 100:.1f}%\n"

    toxicity = results["toxicity"]

    if toxicity < 0.3 :
    
        risk = "LOW"

    elif toxicity >= 0.7 :
    
        risk= "HIGH"

    else:
    
        risk = "MEDIUM"

    final_text = "\nContent Analysis\n" + final_time + "\nRisk level : " + risk + "\n\nDetailed Analysis\n\n" + result

    return final_text