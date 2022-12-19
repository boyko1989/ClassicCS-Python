import CompressedGene
from sys import getsizeof
original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
print("Изначальные данные занимают {} байт".format(getsizeof(original)))

compressed: CompressedGene.ComperssedGene = CompressedGene.ComperssedGene(original)

print("Сжатые данные - {} байт".format(getsizeof(compressed.bit_string)))
print("Сжатие составило {:.2f}%".format(((getsizeof(original) - getsizeof(compressed.bit_string))/getsizeof(original))*100))
if original == compressed.decompress():
    print("Изначальные и распакованные данные равнозначны друг другу")
else:
    print("Изначальные и распакованные данные различаются!!!")
