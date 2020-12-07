
   <!DOCTYPE html>
   <html lang="fr">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       
   </body>
   </html>

<?php
    $connect = mysqli_connect('localhost','saintdi26u','zuugh4Ohta','saintdi26u_3') or die( mysqli_connect_error($connect) ) ;
    $okcharset = mysqli_set_charset($connect, 'utf8');


    $Requete = "SELECT * FROM `etudiants` , `licences` 
    WHERE etudiants.lp=licences.idL ORDER BY `nomL` " ;
    $ResSQLEns = mysqli_query ( $connect , $Requete ) or die ( mysqli_error($connect) ) ;

    $NbEns = mysqli_num_rows($ResSQLEns);

    echo ( '<h1>Nbre étudiants : ' . $NbEns . '</h1>' ) ;

    echo ( '<table>' ) ;

    for ( $Num = 1 ; $Num <= $NbEns ; $Num++ ) {
        $tab = mysqli_fetch_array ( $ResSQLEns ) ;
        echo ( '<tr>
                <td>' . $tab['nom'] . '</td>
                <td>' . $tab['prenom'] . '</td>
                <td><a href="mailto:' . $tab['mail']. '">' . $tab['mail']. '</a></td>
                <td>' . $tab['nomL'] . '</TD>
                <td>' . $tab['departementL'] . '</TD>
                </tr>'
                ) ; }

     echo ( '</table>' ) ;

    $ok = mysqli_free_result ( $ResSQLEns ) ;

    $ok = mysqli_close ( $connect ) ;

?>
