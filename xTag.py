def generate_img_tag(src, alt):
    # Create the <img> tag with src, alt, and max-width: 100%
    img_tag = f'<img src="{src}" alt="{alt}" style="max-width: 100%;">'
    return img_tag

def generate_a_tag(href, anchor_text):
    # Create the <a> tag with href and anchor text
    a_tag = f'<a href="{href}">{anchor_text}</a>'
    return a_tag

def generate_tags(choice):
    if choice == '1':
        img_src = input("Enter the image URL: ")
        img_alt = input("Enter the alt text for the image: ")
        img_tag = generate_img_tag(img_src, img_alt)
        print("\nGenerated <img> tag:")
        print(img_tag)
    elif choice == '2':
        href = input("Enter the link URL: ")
        anchor_text = input("Enter the anchor text for the link: ")
        a_tag = generate_a_tag(href, anchor_text)
        print("\nGenerated <a> tag:")
        print(a_tag)
    else:
        print("Invalid choice")

def main():
    print("\n")
    print("xTags by: Derek Johnston\n")
    while True:
        print("\nMenu:")
        print("1. Generate <img> tag")
        print("2. Generate <a> tag")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1' or choice == '2':
            generate_tags(choice)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
