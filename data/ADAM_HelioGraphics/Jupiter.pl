stk.v.11.0
WrittenBy    STK_v11.3.0

BEGIN Planet

    Name		 Jupiter

    BEGIN PathDescription

        CentralBody		 Jupiter
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 4

            JplSpiceId		 599

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		 2.4515450000000000e+06
            OrbitMeanDist		 7.7841202313279004e+11
            OrbitEcc		 4.8392659999999997e-02
            OrbitInc		 2.3233623726324002e+01
            OrbitRAAN		 3.2543575061605998e+00
            OrbitPerLong		 1.5019945665606999e+01
            OrbitMeanLong		 3.4670475665607000e+01
            OrbitMeanDistDot		 2.4876456756166999e+03
            OrbitEccDot		 -3.5263518138260999e-09
            OrbitIncDot		 -2.0487360627971999e-07
            OrbitRAANDot		 -1.4970999423187999e-07
            OrbitPerLongDot		 6.3732431943192001e-06
            OrbitMeanLongDot		 8.3086747568238001e-02

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		 1.2668653500000000e+17
        Radius		 7.1492000000000000e+07
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

