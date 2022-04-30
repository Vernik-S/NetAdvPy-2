pattern_FIO = r"([а-яёА-ЯЁ]+)"
pattern_phone = r"(\+7|8)(\s|\()*(\d{3})(\s|\)|-)*(\d{3})(\s|-)*(\d{2})(\s|-)*(\d{2})"
sub_pattern = r"+7(\3)\5-\7-\9"

pattern_phone_add = r"\(?(доб\.)+\s(\d+)\)?"
sub_add_pattern = r"\1\2"