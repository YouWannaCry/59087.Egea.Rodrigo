from repository import Repository


class MemberService:

    id_counter = 1

    def __init__(self):
        pass

    def add_member(self, member):
        member.id = MemberService.id_counter
        Repository.membersList[MemberService.id_counter] = member.__dict__
        MemberService.id_counter += 1
        return member.id

    def delete_member(self, id):
        if id < MemberService.id_counter or id == 0:
            Repository.membersList[id] = None
        else:
            raise ValueError("El id no existe")

    def update_member(self, id, member):
        try:
            if id < MemberService.id_counter or id == 0:
                Repository.membersList[id] = member.__dict__
                return
            raise KeyError
        except KeyError:
            raise ValueError
