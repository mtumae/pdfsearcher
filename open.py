import time

from PyPDF2 import PdfReader

filep = "Documentation.pdf"
reader = PdfReader(filep)
pageNumber = len(reader.pages)
queryNumber = 0


query = input("Search for text: ")
start_time = time.perf_counter()

while queryNumber != len(reader.pages):
    text = reader.pages[queryNumber].extract_text()
    if query in text:
        print(
            f"Found '{query}' on page {queryNumber + 1} at position {text.index(query)}"
        )
        res = []
        for i in range(text.index(query), 50):
            res.append(text[i])

        print("".join(res) + ".................")
        print("")

    queryNumber += 1


end_time = time.perf_counter()
print(f"Search complete in {(end_time - start_time):.6f}s")
