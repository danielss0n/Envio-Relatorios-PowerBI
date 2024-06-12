import atualizar_maquinas_sfm
import atualizar_solda_diaria
import atualizar_soldadores
import enviar_email_relatorios

atualizar_maquinas_sfm.init()
atualizar_solda_diaria.init()
atualizar_soldadores.init()

enviar_email_relatorios.send_email("sfm maquinas", "email1@ex.com; email2@ex.com", "email3@ex.com")
enviar_email_relatorios.send_email("solda diaria", "email1@ex.com; email2@ex.com", "")
enviar_email_relatorios.send_email("soldadores", "email1@ex.com; email2@ex.com; email3@ex.com", "")