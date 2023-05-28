class Author:

    all = []

    def __init__(self, name, contracts=None):
        self.name = name
        self._contracts = []
        if contracts:
            for contract in contracts:
                self.add_contracts(contract)
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def add_contracts(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):

        royalties_earnings = []

        for contract in Contract.all:
            if contract.author == self:
                royalties_earnings.append(contract.royalties)
        
        return sum(royalties_earnings)

    
class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
            author.add_contracts(self)
            book.add_authors(author)
        else:
            raise Exception
        if isinstance(book, Book):
            self.book = book
            book.add_contracts(self)
        else:
            raise Exception
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls, date=0):

        return sorted(cls.all, key=lambda contract: contract.date)


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []
        for contract in Contract.all:
            if contract.book == self:
                self._authors.append(contract.author)
        for contract in Contract.all:
            if contract.book == self:
                self._contracts.append(contract)

    def contracts(self):
        return self._contracts

    def add_contracts(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception
        
    def authors(self):
        return self._authors
    
    def add_authors(self, author):
        if isinstance(author, Author):
            self._authors.append(author)
