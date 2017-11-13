formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "lovers come and lovers go",
    "the love that was and the love that should have been",
    "listen, close and softly you might be able to hear it",
    "keep waiting, it will come"
))
