from information_handler import InformationHandler

handler = InformationHandler()

input_source = input(
    "Choose input source from a 'file', 'json', 'xml', or 'console'? (file/json/xml/console): ").strip().lower()

info = None
if input_source in ('file', 'json', 'xml'):
    path = input(f"Please enter the path to the input {input_source}: ").strip()
    handler.process_and_delete(path, input_source)
elif input_source == 'console':
    info = handler.get_information_from_console()
    info.append_info_to_file()
else:
    print("Invalid input source provided. Please enter 'file', 'json', 'xml', or 'console'.")
