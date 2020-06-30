from enum import Enum

class Permissions(Enum):
    # For default users
    Default = 0
    # For admins
    # Has the ability to add, remove, edit data.
    Admin = 1
    # For professionals
    # Has the ability to upload videos.  These videos will automatically
    #   be uploaded to the Youtube channel as private.
    Professional = 2