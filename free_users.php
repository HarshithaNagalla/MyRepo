<?php
//      echo \'start\';
#       echo "<pre>";
        /* give details of host, user, and password of database   */
        $mysqlCommand = "mysql -h HOST -u USER -pPASSWORD$ DATABASE -N -e ";
        echo shell_exec($mysqlCommand. '"SELECT -----QUERY"');
#       echo "</pre>";
//      echo \'the end\';
?>

