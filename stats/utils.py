from django.db.models import Q


def q_search_users(query):
    keywords = [word for word in query.split() if len(word) > 2]

    q = Q()

    for token in keywords:
        q = q | Q(username__icontains=token)
        q = q | Q(first_name__icontains=token)
        q = q | Q(last_name__icontains=token)
        q = q | Q(email__icontains=token)
        q = q | Q(profile__middle_name__icontains=token)

    return q


def q_search_checks(query):
    keywords = [word for word in query.split() if len(word) > 2]

    q = Q()

    for token in keywords:
        q = q | Q(title__icontains=token)
        q = q | Q(body__icontains=token)

    return q
