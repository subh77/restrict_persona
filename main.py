# import utils.user_input as user_input, utils.alpha_model as alpha_model
from utils import user_input, alpha_model
#, context_ops, user_input, role_flow_01

def runtime():
    val = alpha_model.AIMemory().cache_memory()
    print(val)
    return val


# if __name__ == "__main__":
val = runtime()