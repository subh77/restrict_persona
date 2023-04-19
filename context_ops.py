import role_flow_01

candidate_details = role_flow_01.RolesManagement().role_ops()
print(candidate_details)
# message = [{"user":""}]
class RuntimeCache:
    def __init__(self):
        self.role = input("Select role: \n 1 for python developer interview \n 2 for other \n")

    def limiter(self):
        if self.role == "1":
            job_stage = input("Input the correct interview stage i.e. SD1, SD2 or SD3: \n")
            if job_stage not in ["SD1", "SD2", "SD3"]:
                job_stage = "SD3"
            message = [{"role":"user", "content":f"I want you to behave as someone taking an interview for {job_stage} python developer. The candidate will submit the code snippets for the given questions. Your job is to grade each question and give a score ranging from 1 to 10, then grade the candidate on an overall percentage scale. If you find any escape sequences then remove those and then grade the candidate's code"}]
            print(message)

RuntimeCache().limiter()