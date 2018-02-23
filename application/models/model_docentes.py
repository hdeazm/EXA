import web
import config

db = config.db


def get_all_docentes():
    try:
        return db.select('docentes')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_docentes(id_docente):
    try:
        return db.select('docentes', where='id_docente=$id_docente', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_docentes(id_docente):
    try:
        return db.delete('docentes', where='id_docente=$id_docente', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_docentes(nom_doc,especialidad,telefono,direccion):
    try:
        return db.insert('docentes',nom_doc=nom_doc,
especialidad=especialidad,
telefono=telefono,
direccion=direccion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_docentes(id_docente,nom_doc,especialidad,telefono,direccion):
    try:
        return db.update('docentes',id_docente=id_docente,
nom_doc=nom_doc,
especialidad=especialidad,
telefono=telefono,
direccion=direccion,
                  where='id_docente=$id_docente',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
