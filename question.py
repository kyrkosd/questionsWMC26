q=input("How/Where do you find QA/SAST tools? (Individual research, Trusted CO-worker/friend, Ads): ")
q1=input("Do you use QA/SAST tools in your software development process? (yes/no): ")
if q1.lower() == "yes":
    q2=input("What for? (Work, Personal Projects, Both): ")
    if q2.lower() == "work":
        q3=input("Do you find them helpful? (yes/no): ")
        if q3.lower() == "yes":
            q31=input("whould you incorporate them in your personal projects? (yes/no): ")
        elif q3.lower() == "no":
            q32=input("Why not? (Too complex, Not useful, Too Much Noise, Dont know how to use them properly): ")
    elif q2.lower() == "personal projects":
        q4=input("How often do you use them? (Always, Often, Sometimes, Rarely): ")
        q7=input("Do you find them helpful? (yes/no): ")
    elif q2.lower() == "both":
        q5=q4
        q8=q7
elif q1.lower() == "no":
    q9=input("Why not? (Dont know about them, Don't trust them, Expensive, Too much noise): ")
    q10=input("Whould you consider using them in the future? (yes/no): ")
