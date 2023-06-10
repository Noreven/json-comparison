class Result:
    action: str

    def __init__(self, attr_, ref_, change) -> None:
        if len(attr_.split("/")) > 1 and ref_ is None:
            attr_ = attr_.split("/")
            ref_ = attr_.pop(-1)
            attr_ = "/".join(attr_)
        self.attribute = attr_
        self.ref = ref_
        self.change = change


class Create(Result):
    action: str = "CREATE"


class Delete(Result):
    action: str = "DELETE"


class Update(Result):
    action: str = "UPDATE"
