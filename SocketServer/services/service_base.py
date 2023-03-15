#CONFIG
    #Put your configuration options here

#MAIN CODE
def run():
    from lib import VisualEffect as ve
    output = ve.cyan("Service: service_base")+"\n" # Replace the "service_base" with your service name

    try:
        output+=ve.yellow(" > ")+"Print Line!\n"  # Do not use prints! Use this format to make prints! Replaces the "Print line!" for the message to be printed.
                                                  # print("Test")  -->  output+=ve.yellow(" > ")+"Test\n"
        #Code Here



        output+=ve.yellow(" > ")+ve.green("Service completed successfully!\n")
    except Exception as ex:
        return ve.red("Service has not been completed!\nError: "+str(ex)+"\n")

    return output

