import time

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all_contracts = []
    _contract_id = 0

    def __init__(self, author, book, date, royalties=0):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be of type str")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("royalties must be a non-negative number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.id = Contract._contract_id
        Contract._contract_id += 1

        Contract.all_contracts.append(self)
        author._contracts.append(self)
        book._contracts.append(self)

        if book not in author._books:
            author._books.append(book)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = [contract for contract in cls.all_contracts if contract.date == date]
        return sorted(contracts_on_date, key=lambda contract: contract.id)
        