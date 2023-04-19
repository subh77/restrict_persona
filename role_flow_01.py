import pandas as pd


class RolesManagement():
    def __init__(self):
        self.df = pd.read_json("roles.json")
    def role_ops(self):
        eid = input("Enter your email id: ")
        if eid in self.df.email.values:
            # print(self.df)
            # level = self.df.loc[self.df["email"] == eid, "level"].item()
            return(eid, self.df.loc[self.df["email"] == eid, "level"].item())
        else:
            tdf = {"email":eid, "level":"2"}
            self.df = (self.df)._append(tdf, ignore_index=True, sort=False)
            self.df.to_json("roles.json", orient="records")
            # print(self.df)
            return(eid, self.df.loc[self.df["email"] == eid, "level"].item())

