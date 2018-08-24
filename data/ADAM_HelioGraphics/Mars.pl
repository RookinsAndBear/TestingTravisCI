stk.v.11.0
WrittenBy    STK_v11.3.0

BEGIN Planet

    Name		 Mars

    BEGIN PathDescription

        CentralBody		 Mars
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 3

            JplSpiceId		 499

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		 2.4515450000000000e+06
            OrbitMeanDist		 2.2793663617528000e+11
            OrbitEcc		 9.3412330000000002e-02
            OrbitInc		 2.4677208276718002e+01
            OrbitRAAN		 3.3758259393108001e+00
            OrbitPerLong		 3.3633376729917001e+02
            OrbitMeanLong		 3.5574624729917002e+02
            OrbitMeanDistDot		 -2.9575529617247997e+02
            OrbitEccDot		 3.2585900068445999e-09
            OrbitIncDot		 4.8386904489216999e-08
            OrbitRAANDot		 -7.4964810511595998e-07
            OrbitPerLongDot		 1.1805536709966000e-05
            OrbitMeanLongDot		 5.2403297064431997e-01

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		 4.2828375641000000e+13
        Radius		 3.3961900000000000e+06
        Magnitude		 0.0000000000000000e+00
        ReferenceDistance		 0.0000000000000000e+00

    END PhysicalData

    BEGIN AutoRename

        AutoRename		 Yes

    END AutoRename

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals
        END AccessConstraints

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #d292e2
                LabelColor		 #d292e2
                LineColor		 #d292e2
                LineStyle		 0
                LineWidth		 2
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 Off
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 Off
                ShowSubPlanetLabel		 Off
                ShowOrbit		 On
                NumOrbitPoints		 360
                OrbitTime		 7.6005607031260002e+06
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

