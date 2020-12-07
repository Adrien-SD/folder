<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Adrien Saint-Dizier">
    <meta name="generator" content="Jekyll v4.1.1">
    <title>Athome</title>

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


    $Requete = "SELECT * FROM `immo_categories` ORDER BY `nomc` " ;
    $ResSQLEns = mysqli_query ( $connect , $Requete ) or die ( mysqli_error($connect) ) ;
    $ResSQLEns2 = mysqli_query ( $connect , $Requete ) or die ( mysqli_error($connect) ) ;

    $NbEns = mysqli_num_rows($ResSQLEns);

    $Requeteb = "SELECT * FROM `immo_biens` ORDER BY `nomb` " ;
    $ResSQLEnsb = mysqli_query ( $connect , $Requeteb ) or die ( mysqli_error($connect) ) ;

    $NbEnsb = mysqli_num_rows($ResSQLEnsb);




    ?>

    <main role="main" class="container">

        <div class="jumbotron">
            <div class="line">
                <figure><img src="medias/logo/logo.png" alt="Logo" /></figure>
                <h1 class="display-4">Bienvenue chez @Home</h1>
            </div>
            <p class="lead">"Notre agence de construction, près de vous, avec vous pour votre maison !</p>
            <hr class="my-4">
        </div>

        <div class="row">
            <?php     for ( $Num = 1 ; $Num <= $NbEns ; $Num++ ) {
        $tab = mysqli_fetch_array ( $ResSQLEns ) ;
        echo ( '<div class="col-md-4">
                    <h2>Maison "'.$tab['nomc'].'"</h2>
                    <p class="text-justify">'.$tab['descc'].'</p>
                    <p><a class="btn btn-success btn-lg btn-block" href="afficheCategorie.php?idcat='.$tab['idc'].'&nomcat='.$tab['nomc'].' role="button">Voir nos maisons <span class="italic">'.$tab['nomc'].'</span> &raquo;</a></p>
                    </div>
               ' ) ; }
            
                ?>
        </div>

        <div id="carouselExampleCaptions" class="carousel slide col-md-6 offset-md-3 -auto" data-ride="carousel"> <!-- col-md-6 : taille de collonne / 12 | offset-md-3 : décalage des collonnes /12 -->
            <ol class="carousel-indicators">
                <?php 
                    for ( $Num = 1 ; $Num <= $NbEnsb ; $Num++) {
                        $ch = '';
                        if($Num == 1 ) {
                            $ch = 'class="active"';  
                        }
                        echo ( ' <li data-target="#carouselExampleCaptions" data-slide-to="'.$Num.'" '.$ch.'"></li> ') ;
                    }
                ?>
            </ol>
            <div class="carousel-inner  ">
                <?php 
                for ( $Num = 1 ; $Num <= $NbEnsb ; $Num++ ) {
                    $tab2 = mysqli_fetch_array ( $ResSQLEnsb ) ;
                    $ch = '';
                    if($Num == 1) {
                        $ch = ' active';
                    }
                    echo ( ' <div class="carousel-item'.$ch.' ">
                                <img src="medias/biens/'.$tab2['mediab'].'" class="d-block w-100" alt="'.$tab2['nomb'].'">
                                <div class="carousel-caption d-none d-md-block">
                                    <h5>Maison '.$tab2['nomb'].'</h5> 
                                </div>
                            </div>' ) ; }
               
                ?>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>

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

?>