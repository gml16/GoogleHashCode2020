
class Library():
    def __init__(self, _id, books, signing_time, scanning_capacity):
        self.id = _id
        self.books = books
        self.sign_time = signing_time
        self.scan_cap = scanning_capacity
        self.is_sorted = False
        self.score_each_day = [0]
    

    def __hash__(self):
        return hash(hash(self.id) + hash(self.sign_time))

    def __repr__(self):
        return f"<Library {[b.id for b in self.books]}>"

    def sort_books(self):
        import operator
        if not self.is_sorted:
            self.books = sorted(self.books, key=operator.attrgetter('value'), reverse=True)
            self.is_sorted = True

    def score(self, days_left, void_books=set()):
        if len(self.score_each_day) > days_left:
            return self.score_each_day[max(days_left, 0)]
        self.sort_books()
        days_done = len(self.score_each_day) - 1
        scores_to_add = []
        total_score = self.score_each_day[-1]
        book_num = days_done * self.scan_cap
        while days_done < days_left and book_num < len(self.books):
            for i in range(self.scan_cap):
                if book_num >= len(self.books):
                    break
                total_score += self.books[book_num].value if self.books[book_num].id not in void_books else 0
                book_num += 1
            scores_to_add.append(total_score)
            days_done += 1
        self.score_each_day += scores_to_add
        return self.score_each_day[-1]

    def set_max_value(self):
        self.max_score = self.score_each_day[-1] / self.sign_time


class Book():
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"<Book {self.id}, val {self.value}>"
