from validador import Validador as vl

adj = [
       ('RDS','AGN',20.8),('RDS','LAU',26.6),('RDS','TRC',40.8),('RDS','LON',12.8),('RDS','AUR',28),('RDS','PSR',101.1),
       ('AGN','RDS',20.8),('AGN','TRC',23.2),('AGN','PSR',75.3),('AGN','LAU',9.1),
       ('LAU','RDS',26.6),('LAU','AGN',9.1),('LAU','PSR',97.2),
       ('TRC','AGN',23.2),('TRC','RDS',40.8),('TRC','PSR',55.2),('TRC','BRT',14.4),('TRC','AGR',27.4),
       ('LON','RDS',12.8),
       ('AUR','RDS',28),('AUR','ITU',26.6),
       ('OTA','BRT',85.14),
       ('PSR','RDS',101.1),('PSR','LAU',97.2),('PSR','AGN',75.3),('PSR','TRC',55.2),
       ('AGR','TRC',27.4),('AGR','ATA',6.1),('AGR','BRT',30.8),
       ('BRT','AGR',30.8),('BRT','OTA',85.14),('BRT','TRC',14.4),
       ('ITU','ATA',47.96),('ITU','AUR',26.6),('ITU','VID',63.2),('ITU','ALF',113),('ITU','PET',38),
       ('ATA','ITU',47.96),('ATA','AGR',6.1),
       ('PET','ITU',38),
       ('VID','ITU',63.2),
       ('ALF','ITU',113),  
      ] 

ini = input('Origem -> ')
dest = input('Destino -> ')

validador = vl()
validador.validar(ini,dest,adj)