def extract_info(generated_text):
    lines = generated_text.split('\n')
    score = ''
    sentiment = ''
    international_perspective = ''

    for line in lines:
        if "score:" in line.lower():
            is_score = False
            for char in line:
                if char.isdigit() or ord(char) == 46:
                    score += char
                    is_score = True
                elif is_score and not char.isdigit() and ord(char) != 46:
                    break
        elif "sentiment:" in line.lower():
            if "positive" in line.lower():
                sentiment = "Positive"
            elif "negative" in line.lower():
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
        elif "international perspective:" in line.lower():
            if "true" in line.lower():
                international_perspective = True
            else:  
                international_perspective = False

    return sentiment, score, international_perspective