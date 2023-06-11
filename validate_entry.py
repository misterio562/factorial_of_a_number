def validate_entry(new_value):
        if new_value.isdigit() or new_value == "":
            return True
        else:
            return False