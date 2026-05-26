def security_check_basic(user_input):
    
    blocked_terms=["密码","root","删除","sql injection"]
    for term in blocked_terms:
        if term in user_input.lower():
            return False, f"'{term}' should not appear in your input"
        
        
    if len(user_input)>200:
        return False, f"the input is too long..."
    
    return True, "the input passes the basic test"


from transformers import pipeline
classifier=pipeline("text-classification",model="unitary/toxic-bert")


def security_check_unitary(user_input):
    result=classifier(user_input)
    #output: [{'label': 'toxic', 'score': 0.99}]
    
    label=result[0]['label']
    score=result[0]['score']
    
    if score>0.7 and label=='toxic':
        return False,f"({label},{score}) detected!"
    
    return True, "this input passes the unitary test"

def main():
    print("program starts")
    user_input =input("what do you want to ask: ")
    
    is_safe_basic,message1=security_check_basic(user_input)
    is_safe_unitary,message2=security_check_unitary(user_input)
    
    if is_safe_basic and is_safe_unitary:
        print("okay this is sent to AI")
    else:
        if not is_safe_basic:
            print(message1)
        if not is_safe_unitary:
            print(message2)


if __name__=="__main__":
    main()