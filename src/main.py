from textnode import TextType, TextNode

def main():
    test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test)
    return


main()