from HW1_data import records, records_many

# This function accepts an iterable of data records (item examples are below)
# and builds the data structure fulfilling the above requirements.
# ---------------------------------------------------------------------------
# HINT. There is notihing stopping you from adding additional data fields.
# Can it help you solve the problem of non-unique names?
# ---------------------------------------------------------------------------
def build_data_structure(records):
    """Build the data structure for the management system.
    
    Parameters
    ----------
    records : iterable
        Iterable of data records.
    """
    pass

# This function finds a student by name and surname.
# ---------------------------------------------------------
# HINT: remember that names can be non-unique.
# What does it suggest with respect to the type of output?
# ----------------------------------------------------------
def find_by_name(data, name):
    """Find student(s) data by name.
    
    Parameters
    ----------
    data : object
        Data structure as returned by `build_data_structure()`.
    name : str
        Name and surname.
    """
    pass

# This funciton finds a student by id.
# ---------------------------------------------------------
# HINT: ids are guarateed to be unique.
# What does it suggest with respect to the type of output?
# ----------------------------------------------------------
def find_by_idx(data, idx):
    """Find student data by student id.
    
    Parameters
    ----------
    data : object
        Data structure as returned by `build_data_structure()`.
    idx : int
        Student id.
    """
    pass

# This function has to return a list of students at a give program and year.
# ----------------------------------------------------------------------------
# HINT. Remember that you are free to define whatever fields you like
# in your management system data struture.
# ----------------------------------------------------------------------------
def list_students_by_program_and_year(data, program, year):
    """List all students enrolled in a program and at specific year.
    
    Parameters
    ----------
    data : object
        Data structure as returned by `build_data_structure()`.
    program : str
        Name of a program.
    year : int
        Year.
    """
    pass

# This function has to return a list of students enrolled in a given class.
# ---------------------------------------------------------------------------
# HINT. Remeber that you are free to define whatever data fields you like
# and that you can arbitrarily rearrane and copy data.
# ---------------------------------------------------------------------------
def list_students_enrolled_in_class(data, idx):
    """List all students enrolled in a class.
    
    Parameters
    ----------
    data : object
        Data structure as returned by `build_data_structure()`.
    idx : int
        Class id.
    """
    pass
