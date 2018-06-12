class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = []

    def __init__(self,application,username,email,password):

        self.application = application
        self.username = username
        self.email = email
        self.password = password