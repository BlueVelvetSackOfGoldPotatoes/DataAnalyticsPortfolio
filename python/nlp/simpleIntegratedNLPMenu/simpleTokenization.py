import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download()

def sentTokenize(sample) :
 print (word_tokenize(sample))

def sentTokenize(sample) :
 print (word_tokenize(sample))

def main():
    '''
    on console:
        import nltk
        nltk.download()
        d
        all
    '''
    sample = "1.   Whatever is capable of increase or diminution, is called magnitude, or quantity. A sum of money therefore is a quantity, since we may increase it or diminish it. It is the same with a weight, and other things of this nature. 2.   From this definition, it is evident that the different kinds of magnitude must be so various, as to render it difficult to enumerate them and this is the origin of the different branches of Mathematics, each being employed on a particular kind of magnitude. Mathematics, in general, is the science of quantity; or, the science which investigates the means of measuring quantity. 3.   Now, we cannot measure or determine any quantity, except by considering some other quantity of the same kind as known, and point out their mutual relation. If it were proposed, for example, to determine the quantity of a sum of money, we should take some known piece of money, as a louis, a crown, a ducat, or some other coin, and show how many of these pieces are contained in a given sum. In the same manner, if it were proposed to determine the quantity of a weight, we should take a certain known weight; for example, a pound, and ounce, &c., and then show how many times one of these weights is contained in that which we are endeavouring to ascertain. If we wished to measure any length, or extension, we should make use of some known length, such as a foot. 4.   So that the determination, or the measure of magnitude of all kinds, is reduced to this: fix at pleasure upon any one known magnitude of the same species with that which is to be determined, and consider it as the measure or unit; then, determine the proportion of the proposed magnitude to this known measure. This proportion is always expressed by numbers; so that a number is nothing but the proportion of one magnitude to another, arbitrarily assumed a unit. 5.   From this it appears that all magnitudes may be expressed by numbers; and that the foundation of all the Mathematical Sciences must be laid in a complete treatise on the science of numbers, and in an accurate examination of the different possible methods of calculation. This fundamental part of mathematics is called Analysis, or Algebra1. 6.   In Algebra then we consider only numbers, which represent quantities, without regarding the different kinds of quantity. These are the subjects of other branches of mathematics. 7.   Arithmetic treats of numbers in particular, and is the science of number properly so called; but this science extends only to certain methods of calculation which occur in common practice: Algebra, on the contrary, comprehends in general all the cases that can exist in the doctrine and calculation of numbers."

    # per word
   
    # per sentence
    print (sent_tokenize(sample))

'''
Make a menu that enables the user to save the result of tokenizations and what not - basically a program that offers an interface.
'''