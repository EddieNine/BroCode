
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")

