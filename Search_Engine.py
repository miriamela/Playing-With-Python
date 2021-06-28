import os
import string


def main():
    filenames = getting_files()
    index = {}
    file_titles = {}
    creating_index(filenames, index, file_titles)
    while True:
        query = getting_query()
        if query == "":
            print("Thank you for using our search engine! Bye-Bye :)")
            break
        results = searching(index, query)
        show_results(results, file_titles, query)


def getting_query():  # GETTING QUERY FROM USER
    query = input(
        "Enter your query, each word separated by a space or press enter to stop: ")
    query = query.lower()
    return query


def getting_files():  # GETTING ALL DATA
    filenames = []
    directory = "bbcnews"
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".txt"):
            filenames.append(os.path.join(directory, file))
    return filenames


def creating_index(filenames, index, file_titles):
    for each in filenames:
        words = []
        with open(each) as f:
            for line in f:
                if not line.isspace():
                    line = line.strip().split()
                    words.extend(line)

        cleaned_terms = []  # cleaning all terms
        for word in words:
            word = word.strip(string.punctuation).lower()
            if len(word) > 0:
                cleaned_terms.append(word)

        for term in cleaned_terms:  # populating index
            if term not in index:
                index[term] = [each]
            else:
                if each not in index[term]:
                    index[term].append(each)

        with open(each) as f:  # populating file_titles
            title = f.readline()
            if each not in file_titles:
                file_titles[each] = title.strip()

    return index, file_titles


def searching(index, query):
    results = []
    query = query.split(" ")
    if query[0] in index:  # BUILDING FIRST LIST
        for each in index[query[0]]:
            results.append(each)
        query.pop(0)
    else:
        return results
    print("first list results " + str(results))
    if query:
        for word in query:
            if word in index:
                second_results = index[word]  # BUILDING SECOND LIST
                results = comparing_lists(
                    results, second_results)  # COMPARING TWO LISTS
            else:
                results = []
                return results
    return results


def comparing_lists(results, second_results):
    common_results = []
    for result in results:
        if result in second_results:
            common_results.append(result)
    results = common_results
    return results


def show_results(results, file_titles, query):
    if results:
        print("Results for query '" + query + "':")
        for result in results:
            title = file_titles[result]
            print("- " + title)
    else:
        print("No results match that query.")


if __name__ == "__main__":
    main()
