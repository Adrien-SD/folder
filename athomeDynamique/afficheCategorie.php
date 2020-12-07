<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Des maisons pensées pour les familles, faciles à vivre, intégrant toutes les fonctionnalités les plus récentes en termes de domotique, de recyclage des calories. Construite conformément aux dernières normes en vigueur sur l'économie d'énergie et les matériaux recyclables, votre maison vous assure une qualité de vie irréprochable pour longtemps.">
    <meta name="author" content="Adrien Saint-Dizier">
    <meta name="generator" content="Jekyll v4.1.1">
    <title>Modernite - Athome</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.5/examples/starter-template/">

    <!-- Bootstrap core CSS -->
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="/docs/4.5/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
    <link rel="icon" href="/docs/4.5/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="/docs/4.5/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="manifest" href="/docs/4.5/assets/img/favicons/manifest.json">
    <link rel="mask-icon" href="/docs/4.5/assets/img/favicons/safari-pinned-tab.svg" color="#563d7c">
    <link rel="icon" href="/docs/4.5/assets/img/favicons/favicon.ico">
    <meta name="msapplication-config" content="/docs/4.5/assets/img/favicons/browserconfig.xml">
    <meta name="theme-color" content="#563d7c">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .line {
            display: flex;
        }

        .italic {
            font-style: italic;
        }

    </style>
    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">
</head>

<body>
    <?php require ( 'nav.php' ) ; ?>

    <?php
    $connect = mysqli_connect('localhost','saintdi26u','zuugh4Ohta','saintdi26u_3') or die( mysqli_connect_error($connect) ) ;
    $okcharset = mysqli_set_charset($connect, 'utf8');

    $nomcat = $_GET['nomcat'];
    $idcat = $_GET['idcat'];




    $Requete = "SELECT * FROM `immo_biens`  WHERE categorieb = $idcat ORDER BY `nomb` " ;
    $ResSQLEns = mysqli_query ( $connect , $Requete ) or die ( mysqli_error($connect) ) ;
    $ResSQLEns2 = mysqli_query ( $connect , $Requete ) or die ( mysqli_error($connect) ) ;

    $NbEns = mysqli_num_rows($ResSQLEns);








    ?>

    <main role="main" class="container">

        <h1>
            Nos maisons <?php echo ($nomcat.'('.$idcat.')' ) ; ?> <small>Retrouver nos <?php echo($NbEns) ; ?> offres !</small>
        </h1>
        <hr />

        <div class="row">
            <?php for ( $Num = 1 ; $Num <= $NbEns ; $Num++ ) {
            $tab = mysqli_fetch_array ( $ResSQLEns ) ; 
                echo ('<div class="col-sm-6 col-md-4">
                    <div class="card">
                        <img class="card-img-top" src="medias/biens/'.$tab['mediab'].'" alt="Card image '.$tab['nomb'].'">
                        <div class="card-body">
                            <h5 class="card-title">'.$tab['nomb'].'</h5>
                            <p class="card-text">'.$tab['descb'].'</p>
                            <button class="btn btn-primary" data-toggle="modal" data-target="#staticBackdrop'.$tab['idb'].'">Détails</button>
                        </div>
                    </div>
                </div>') ; }?>
        </div>

           

        <!--Modal -->
        <?php for ( $Num = 1 ; $Num <= $NbEns ; $Num++ ) {
            $tab2 = mysqli_fetch_array ( $ResSQLEns2 ) ; 
                echo ('<div class="modal fade" id="staticBackdrop'.$tab2['idb'].'" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Maison "'.$tab2['nomb'].'"</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <figure><img src="medias/biens/'.$tab2['mediab'].'" /></figure>
                            <p>'.$tab2['descb'].'</p>
                            <h5>Indication de performance énergétique : '.$tab2['codeenergieb'].'</h5>
                            <div class="progress">
                                <div class="progress-bar " role="progressbar" style="width: '.$tab2['indiceenergieb'].'%; background-color:');
                                if($tab2['indiceenergieb'] > 80) { echo('green') ;}
                                else if($tab2['indiceenergieb'] < 60) { echo('red') ;}
                                else { echo('orange') ; }
                                echo(';" aria-valuenow="'.$tab2['indiceenergieb'].'" aria-valuemin="0" aria-valuemax="100" >'.$tab2['indiceenergieb'].'</div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>
                        </div>
                    </div>
                </div>
            </div>') ; }?>
        


        <hr />
        <div class="footer">
            <p>&copy; MMI IUTSD</p>
        </div>


    </main><!-- /.container -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script>
        window.jQuery || document.write('<script src="/docs/4.5/assets/js/vendor/jquery.slim.min.js"><\/script>')

    </script>
    <script src="dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>

<?php     
$ok = mysqli_free_result ( $ResSQLEns ) ;

$ok = mysqli_close ( $connect ) ;

?>?>
